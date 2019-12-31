<template>
  <v-app-bar app color="#fff">
    <v-icon>mdi-view-dashboard</v-icon>
    <div class="ml-2"></div>
    <v-toolbar-title>
      <nuxt-link to="/admin" tag="div" class="link">Dashboard</nuxt-link>
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <v-btn color="blue-grey" dark nuxt to="/">回前台</v-btn>
  </v-app-bar>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>