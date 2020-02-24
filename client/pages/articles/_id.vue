<template>
  <v-container style="max-width:768px">
    <h2>{{upperTitle}}</h2>
    <small>{{article.date}}</small>
    <v-list>
      <v-chip label class="mr-1" v-for="(tag,i) in article.tags.split(',')" :key="i">{{tag}}</v-chip>
    </v-list>
    <h3>{{article.preview}}</h3>
    <p>{{article.content}}</p>
    <client-only>
      <vue-disqus shortname="jet-blog" :identifier="article.article_id"></vue-disqus>
    </client-only>
  </v-container>
</template>

<script>
import Vue from "vue";
import VueDisqus from "vue-disqus";
import Article from "~/services/article.js";
Vue.use(VueDisqus);
export default {
  async asyncData({ params }) {
    let data = await Article.get(params.id);
    return {
      article: data
    };
  },
  head() {
    return {
      title: this.article.title
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