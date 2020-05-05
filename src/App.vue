<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
@import "@/styles/variables.scss";
body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,button,textarea,p,blockquote,th,td{ margin: 0; padding: 0;}
ul,ol,li{ list-style: none;}
a{ text-decoration: none;}
html {
  font-size: 14px;
  font-family: PingFangSC-Regular, Verdana, Arial, "微软雅黑", "宋体";
  color: $dark;
  background-color: #f7f9fb;
}
</style>
