<template>
  <header>
    <div class="wapper">
      <div class="logo">
        <span>稳</span>
      </div>
      <div class="search">
        <input type="text" placeholder="查找..." />
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'MergeHeader'
}
</script>

<style lang="scss" scoped>
@import '@/styles/mixin.scss';
header {
  background-color: #222;
  padding-top: 12px;
  margin-bottom: 50px;
  height: 50px;
  .wapper{
      @include wapper;
  }

  .logo {
    float: left;
    span {
      color: #0094c0;
      font-size: 2em;
    }
  }

  .search {
    float: right;

    input {
      width: 200px;
      height: 30px;
      background-color: #FFF;
      border: solid 1px #333;
      padding-left: 8px;
    }
  }
}
</style>
