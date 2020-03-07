<template>
  <div class="hello">
    我是首页
  </div>
  <div class="category">aaa
  </div>
</template>

<script>
export default {
  name: 'Home',
  data(){
    return{
      categoryList:[]
    }
  },
  methods:{
    getCategoryList(){
      this.$https.get('v1/article/index/guess/')
        .then((res)=>{
          console.log(res.data.data);
        })
        .catch((error)=>{
          console.log(error)
        })
    }
  },
  created(){
    this.getCategoryList()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
