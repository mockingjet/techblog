import Vue from 'vue'

import MarkdownIt from 'markdown-it'
import markdownItMark from 'markdown-it-mark'
import markdownItAttrs from 'markdown-it-attrs'
import markdownItContainer from 'markdown-it-container'
import markdownItPlayground from 'markdown-it-playground'
import markdownItHighlightjs from './highlight'

const md = new MarkdownIt({
  html: true,
  breaks: true,
  linkify: true,
  highlight: true,
  typographer: true,
  langPrefix: 'blog-'
})

md.use(markdownItMark)
md.use(markdownItAttrs)
md.use(markdownItPlayground)
md.use(markdownItHighlightjs)


md.use(markdownItContainer, 'accent')
md.use(markdownItContainer, 'warning')
md.use(markdownItContainer, 'error')

Vue.use({
  install(Vue, options) {
    Vue.prototype.$md = md
  }
})