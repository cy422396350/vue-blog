<template>
  <div class="left">
    <div class="overlay"></div>
      <div class="leftContent">
          <nav class="header-menu">
              <ul>
                  <li v-for="item in categories">
                      <router-link :to="'/category/'+item.id" v-text="item.name"></router-link>
                  </li>
              </ul>
          </nav>
      </div>
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

<style lang="scss">
  .overlay{
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.75);
    position: absolute;
    opacity: 0.5;
    z-index: -1;
  }
    .leftContent{
        width: 98%;
        padding-top: 10px;
        text-align: center;
        position: absolute;
        left: 50%;
        top: 50%;
        margin: 40px 0 auto;
        transform: translate(-50%, -50%);;
    }
    nav{
        width: 300px;
        line-height: 30px;
        font-size:24px;
        ul{
            padding: 0;
            li{
                text-align: center;
                a{
                    color:ghostwhite;
                    &:hover{
                        color:deepskyblue;
                    }
                    transition:all 0.6s;
                }
            }
        }
    }

</style>
