<template>
  <v-app-bar app color="white" class="px-12">
    <v-icon>mdi-home</v-icon>
    <div class="ml-2"></div>
    <v-toolbar-title class="font-weight-bold">
      <nuxt-link to="/" tag="div" class="link">JET's Blog</nuxt-link>
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn color="blue" class="mx-1" dark nuxt to="/admin/articles/create">創建文章</v-btn>
    <v-btn color="red" class="mx-1" dark nuxt to="/articles">瀏覽所有文章</v-btn>

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