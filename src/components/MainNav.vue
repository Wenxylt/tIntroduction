<template>
  <nav>
    <ul>
      <li v-for="(crumbItem,index) in crumb" :key="index">
        <a href="#">{{crumbItem}}</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'MainNav',
  data() {
    return {
      crumb: ['首页', '关于我们']
    }
  }
}
</script>

<style lang="scss" scoped>
nav {
  position: absolute;
  top: -2em;
  left: 10px;
  width: 100%;
}
ul {
  height: 2rem;
  li {
    list-style: none;
    font-size: 0.85rem;
    float: left;
    padding-right: 0.5em;
    a {
      color: #333;
      &:hover {
        color: #0094c0;
      }
      padding-right: 0.5em;
    }
    &:after {
      content: ">>";
      color: #ccc;
    }
    &:last-of-type::after {
      content: "";
    }
  }
}
</style>
