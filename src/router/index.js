import Vue from 'vue'
import Router from 'vue-router'
import Guide from '@/components/Guide'
import Index from '@/components/Index'
import Category from '@/components/Category'
import Article from '@/components/Article'

Vue.use(Router)

var router = new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/category/:category',
      name: 'category',
      component: Category
    },
    {
      path: '/guide',
      name: 'guide',
      component: Guide
    },
    {
      path: '/article/:id',
      name: 'article',
      component: Article
    },
  ]
})

router.push({ path: 'guide' })

router.beforeEach((to, from, next) => {
  if(to.name === "guide"){
    router.push({ path: '/' })
    next()
  }else {
    next()
  }
})


export default router
