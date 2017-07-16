<template>
  <article>
    <header>
      <h1 v-text="title"></h1>
      <p><time v-text="time"></time></p>
    </header>
    <p v-text="article"> Windows Internet Explorer 9(缩写为 IE9 )是在2011年3月14日21:00发布的</p>
  </article>
</template>

<script>
  export default {
      name:"article",
      data(){
        return {
            title:null,
            article:null,
            time:null
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
      const url = this.buildUrl(this.$store.state.config.url.article)+"&id="+this.$route.params.id
      this.$http.get(url).then(response => {
        // get body data
        let data = JSON.parse(response.bodyText);
        if(data.showapi_res_code===0){
          this.title = data.showapi_res_body.item.title;
          this.article = data.showapi_res_body.item.userName;
          this.time = data.showapi_res_body.item.ct;
        }
      }, response => {
        // error callback
      });
    }
  }
</script>
