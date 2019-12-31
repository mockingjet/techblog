<template>
  <v-container style="max-width:768px">
    <h2>{{upperTitle}}</h2>
    <h3>{{article.subtitle}}</h3>
    <small>{{article.date}}</small>
    <p>{{article.content}}</p>
  </v-container>
</template>

<script>
import Article from "~/services/article.js";
export default {
  async asyncData({ params }) {
    let data = await Article.get(params.id);
    return {
      article: data
    };
  },
  computed: {
    upperTitle() {
      const titleWords = this.article.title.split(" ");
      const newTitleWords = titleWords.map(
        str => str.charAt(0).toUpperCase() + str.slice(1)
      );
      return newTitleWords.join(" ");
    }
  }
};
</script>

<style lang="scss" scoped>
</style>