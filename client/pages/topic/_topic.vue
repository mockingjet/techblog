<template>
  <v-container>
    <h1>{{topic}}</h1>
  </v-container>
</template>

<script>
export default {
  head() {
    return {
      title: "TechBlog" + " / " + this.topic
    };
  },
  validate({ params }) {
    const topics = ["Frontend", "Backend", "Devops"];
    return topics.includes(params.topic) ? true : false;
  },
  data() {
    return {
      topic: this.$route.params.topic
    };
  }
};
</script>

<style lang="scss" scoped>
</style>