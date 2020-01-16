<template>
  <v-app-bar app dark color="info">
    <v-icon>mdi-view-dashboard</v-icon>
    <div class="ml-2"></div>
    <v-toolbar-title>
      後台管理
      <!-- <nuxt-link to="/admin" tag="div" class="link">後台管理</nuxt-link> -->
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <v-btn color="secondary" dark nuxt to="/">回前台</v-btn>
  </v-app-bar>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>