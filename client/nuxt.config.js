module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'TechBlog',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt.js project' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Server & Client 
  */
  env: {
    HOST_URL: process.env.HOST_URL || 'http://127.0.0.1:5000'
  },
  server: {
    host: '0.0.0.0',
    port: 3000
  },
  /*
  ** Third Party Library
  */
  buildModules: [
    '@nuxtjs/vuetify'
  ],
  vuetify: {},
  plugins: [
    '~/plugins/markdownit',
    { src: '~/plugins/codemirror', ssr: false }
  ],
  /*
  ** Global CSS
  */
  css: [
    '~/assets/css/main.css',
    'highlight.js/styles/default.css',
    'highlight.js/styles/rainbow.css',
    'codemirror/lib/codemirror.css',
    'codemirror/theme/monokai.css'
  ]
}