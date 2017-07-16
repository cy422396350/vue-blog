<template>
  <div class="loader">
    <div class="loader1">
      <div>
        <div>
          <div>
            <div>
              <div>
                <div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
  *{box-sizing: border-box}
  $c1:rgba(0,0,0,0.5);
  $c2:rgba(0,0,184,0.5);

  @keyframes rotate{
    0% {
      transform: rotate(0deg)
    }
    50% {
      transform: rotate(180deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  @mixin lm {
    position: relative;
    margin: 75px auto;
    width: 150px;
    height: 150px;
    display: block;
    overflow: hidden;
  }

  @mixin lmd{
    border-radius: 50%;
    padding:8px;
    border: 2px solid transparent;
    animation: rotate linear 4s infinite;
  }
  @mixin ld{
    height: 100%;
  }
  .loader{
    background: rgba(0,0,0,0.3);
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

  .loader1{
    @include lm;
  }
  .loader1 div{
    @include ld;
    @include lmd;
    border-top-color: $c1;
    border-bottom-color: $c2;
  }
  div:hover {
    animation-play-state: paused;
  }

  .loader1, .loader * {
    will-change: transform;
  }
</style>

<script>
  export default {
    name: 'loading'
  }
</script>
