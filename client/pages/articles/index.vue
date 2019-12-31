<template>
  <v-container style="max-width:768px">
    <section v-for="(article,i) in articles" :key="i">
      <h3>{{article.title}}</h3>
      <small>{{article.date}}</small>
      <p>{{article.content}}</p>
      <v-btn color="red" dark nuxt :to="`/articles/${article.id}`">read</v-btn>
    </section>
  </v-container>
</template>

<script>
import Article from "~/services/article.js";
export default {
  async asyncData() {
    let data = await Article.all();
    console.log(data);
    return {
      articles: data
    };
  }
};
</script>

<style>
h1 {
  font-size: 40px;
}
p {
  font-size: 20px;
}
</style>