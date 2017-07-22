<template>
  <transition name="fade" mode="out-in">
    <loading v-if="!image" key="loading"></loading>
    <div class="guide" v-if="image" key="guide">
      <div class="inner" v-bind:class="{ lighter: image}">
        <p>{{name}}</p>
        <hr>
        <p class="title">{{title}}</p>
        <hr class="secondary">
        <router-link to="/" class="view">{{enter}}</router-link>
      </div>
    </div>
  </transition>
</template>

<script>
  import Loading from './Loading.vue'
export default {
  components:{Loading},
  name: 'hello',
  data () {
    return {
      name:'常中蝎',
      enter: 'View',
      title: '嗨，我是常中蝎，一名来自 2.5 次元的魔法师，目前就读于河南工业大学，魔法学院，土木工程专业。',
      isimage:0
    }
  },
  computed:{
    image () {
      return this.isimage?1:0;
    }
  },
  created () {
      var self = this;
      var backgroud = new Image();
      backgroud.src = "http://ossz5roem.bkt.clouddn.com/ed1e68ab58a1b7b4513ca3eea0211fc7.jpg"
      if(backgroud.complete){
        self.isimage = 1;
      }else{
          backgroud.onload = function () {
            self.isimage = 1;
          }
      }
  },
  destroyed(){
      this.$emit("showbox",1)
  }
}
</script>

<style lang="scss">
  @import '../assets/style/global.scss';
  $whiteColor: #fff;
  $border: 1px solid #DF9C81;
  @mixin backgroundCover($url) {
    background: url($url) no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }
  @mixin elementIn($time){
    -webkit-animation: bounceInLeft 1.2s linear ($time) backwards;
    -moz-animation: bounceInLeft 1.2s linear ($time) backwards;
    -ms-animation: bounceInLeft 1.2s linear ($time) backwards;
    animation: bounceInLeft 1.2s linear ($time) backwards;
  }
  @-webkit-keyframes myfirst
  {
    from {background: rgba(0,0,0,.4);}
    to {background:transparent}
  }

  .lighter{
    animation:myfirst 1s;
    -webkit-animation: myfirst 1s linear 1s backwards;
  }
  .inner{
    width: 100%;
    height: 100vh;
    max-height: 100%;
    overflow: hidden;
    line-height: 100%;
    display: flex;
    align-items: center;
    flex-direction:column;
    justify-content: center;
  }
  .guide {
    @include backgroundCover("http://ossz5roem.bkt.clouddn.com/ed1e68ab58a1b7b4513ca3eea0211fc7.jpg");
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    width: 100%;
    height: 100vh;
    max-height: 100%;
    overflow: hidden;
    line-height: 100%;
    color: $whiteColor;
    .secondary{
      width: 15%;
    }
    hr{
      width: 50%;
      margin: 20px auto;
      border-top: 1px solid rgba(255, 255, 255, 0.14);
    }
    p{
      @include elementIn(0s);
      font-size: 1.9em;
      padding: 1em 2em;
    }
    p.title{
      @include elementIn(0.5s);
      line-height: 1.7em;
      font-size: .9em;
      padding: 1em 2em;
    }
    a {
      @include elementIn(1s);
      border: $border;
      text-decoration: none;
      display: block;
      position: relative;
      border-color: #FFF;
      color: #FFF;
      padding: 10px 20px;
      border-radius: 20px;
      opacity: .8;
    }
    .view{
      transition: all 0.6s;
    }
    .view:hover{
      background-color: $white;
      color: $black;
      font-weight: bold;
      transform: scale(1.2);
    }
  }
</style>
