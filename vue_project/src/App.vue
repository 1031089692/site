<template>
  <div id="app">
    <el-container>
      <el-header>
        <router-link :to="{name:'Home'}">首页</router-link>
        <router-link :to="{name:'Course'}">免费课程</router-link>
            <router-view/>
      </el-header>
      <el-main>
        ---
      </el-main>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: 'App',

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
