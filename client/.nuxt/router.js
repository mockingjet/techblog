import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _9d54f0fa = () => interopDefault(import('..\\pages\\about.vue' /* webpackChunkName: "pages_about" */))
const _7d4269b7 = () => interopDefault(import('..\\pages\\articles.vue' /* webpackChunkName: "pages_articles" */))
const _142edeeb = () => interopDefault(import('..\\pages\\articles\\index.vue' /* webpackChunkName: "pages_articles_index" */))
const _792da013 = () => interopDefault(import('..\\pages\\articles\\_id.vue' /* webpackChunkName: "pages_articles__id" */))
const _63cfc484 = () => interopDefault(import('..\\pages\\admin\\articles\\create.vue' /* webpackChunkName: "pages_admin_articles_create" */))
const _87be1256 = () => interopDefault(import('..\\pages\\topic\\_topic.vue' /* webpackChunkName: "pages_topic__topic" */))
const _5de53b70 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages_index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/about",
    component: _9d54f0fa,
    name: "about"
  }, {
    path: "/articles",
    component: _7d4269b7,
    children: [{
      path: "",
      component: _142edeeb,
      name: "articles"
    }, {
      path: ":id",
      component: _792da013,
      name: "articles-id"
    }]
  }, {
    path: "/admin/articles/create",
    component: _63cfc484,
    name: "admin-articles-create"
  }, {
    path: "/topic/:topic?",
    component: _87be1256,
    name: "topic-topic"
  }, {
    path: "/",
    component: _5de53b70,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
