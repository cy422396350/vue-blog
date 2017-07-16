<template>
  <nav class="header-menu">
    <ul>
      <li v-for="item in categories">
        <router-link :to="item.url" v-text="item.title"></router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
  export default{
    name:'vue-footer',
    data(){
      return {
        categories:[
          {
            title:'Linux',
            url:'/category/linux'
          },
          {
            title:'PHP',
            url:'/category/php'
          },
          {
            title:'Database',
            url:'/category/database',
          }
        ]
      }
    }
  }
</script>
