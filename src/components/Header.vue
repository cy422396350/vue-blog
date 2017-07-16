<template>
  <div class="wrapper">
    <nav class="header-menu">
      <ul>
        <li v-for="item in categories">
          <router-link :to="'/category/'+item.id" v-text="item.name"></router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default{
  name:'vue-header',
  data(){
    return {
      categories: null
    }
  },
  created(){

    /**
     * 获取类别：https://route.showapi.com/90-86?
     * showapi_appid=42417
     * &
     * showapi_test_draft=false
     * &
     * showapi_timestamp=20170716212524
     * &
     * showapi_sign=664b6bfeb4edf136d46ab405319e742c
     */
    const categoryUrl = this.buildUrl(this.$store.state.config.url.category)
    this.$http.get(categoryUrl).then(response => {
      // get body data
      let data = JSON.parse(response.bodyText);
      if(data.showapi_res_code===0){
        this.categories = data.showapi_res_body.typeList;
      }
    }, response => {
      // error callback
    });
  }
}
</script>
