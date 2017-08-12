<template>
  <transition appear name="page" mode="out-in">
  <div class="right">
    <div class="right-content article">
      <header>
        <h1 v-text="title"></h1>
        <p><time v-text="time"></time></p>
      </header>
      <article v-html="article"> Windows Internet Explorer 9(缩写为 IE9 )是在2011年3月14日21:00发布的</article>
    </div>
  </div >
  </transition>
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
      //const url = this.buildUrl(this.$store.state.config.url.article)+"&id="+this.$route.params.id
      let url = this.$store.state.apiUrl+"article/"+this.$route.params.id
      this.$http.get(url).then(response => {
        // get body data
        let data = JSON.parse(response.bodyText);
          this.title = data.title;
          this.article = data.content;
          this.time = data.time;
      }, response => {
        // error callback
      });
    }
  }
</script>
<style lang="scss">
  .article{
    header{
      margin: 0 0 30px 30px;
    }
    article{
      padding:0 10px;
      line-height: 1.5;
    }
  }
</style>
