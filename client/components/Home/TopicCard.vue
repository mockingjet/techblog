<template>
  <v-card link nuxt :to="item.link">
    <v-card-title>
      {{item.title}}
      <v-icon>{{item.icon}}</v-icon>
    </v-card-title>
    <v-card-subtitle>{{item.subtitle}}</v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      default: {
        title: "",
        icon: "",
        link: "",
        subtitle: ""
      }
    }
  }
};
</script>

<style lang="scss" scoped>
</style>