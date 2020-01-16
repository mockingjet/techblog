<template>
  <v-app-bar app dark color="secondary">
    <v-icon>mdi-home</v-icon>
    <div class="ml-2"></div>
    <v-toolbar-title>
      <nuxt-link to="/" tag="div" class="link">Tech Blog</nuxt-link>
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn color="blue" dark nuxt to="/admin/articles/create">創建文章</v-btn>
    <v-btn color="red" dark nuxt to="/articles">瀏覽文章</v-btn>

    <v-btn icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>mdi-heart</v-icon>
    </v-btn>
    <v-btn icon>
      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>