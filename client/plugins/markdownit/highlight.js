import hljs from 'highlight.js/lib/highlight'

import bash from 'highlight.js/lib/languages/bash'
import css from 'highlight.js/lib/languages/css'
import javascript from 'highlight.js/lib/languages/javascript'
import python from 'highlight.js/lib/languages/python'
import cpp from 'highlight.js/lib/languages/cpp'

hljs.registerLanguage('bash', bash)
hljs.registerLanguage('css', css)
hljs.registerLanguage('javascript', javascript)
hljs.registerLanguage('python', python)
hljs.registerLanguage('cpp', cpp)

const maybe = f => {
  try {
    return f()
  } catch (e) {
    return false
  }
}

// Highlight with given language.
const highlight = (code, lang) =>
  maybe(() => hljs.highlight(lang, code, true).value) || ''

// Highlight with given language or automatically.
const highlightAuto = (code, lang) =>
  lang
    ? highlight(code, lang)
    : maybe(() => hljs.highlightAuto(code).value) || ''

// Wrap a render function to add `hljs` class to code blocks.
const wrap = render =>
  function (...args) {
    const styles = `
    style="
      box-shadow:unset;
      background-color:#1C1D21;
      color: #c0c5ce;
      display:block;
      padding: 0.5em;
      font-size: 100%;
    "`

    return render.apply(this, args)
      .replace('<code class="', `<code ${styles} class="hljs `)
      .replace('<code>', `<code ${styles} class="hljs">`)
  }


const highlightjs = (md, opts) => {
  opts = Object.assign({}, highlightjs.defaults, opts)

  md.options.highlight = opts.auto ? highlightAuto : highlight
  md.renderer.rules.fence = wrap(md.renderer.rules.fence)

  if (opts.code) {
    md.renderer.rules.code_block = wrap(md.renderer.rules.code_block)
  }
}

highlightjs.defaults = {
  auto: true,
  code: true
}

export default highlightjs