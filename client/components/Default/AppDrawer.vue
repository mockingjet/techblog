<template>
  <v-navigation-drawer app v-model="drawer">
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
        <v-list-item-title>John Leider</v-list-item-title>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense>
      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <nuxt-link :to="{name:item.to}">
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </nuxt-link>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ["drawer"],
  data() {
    return {
      items: [
        { title: "Home", icon: "mdi-home", to: "index" },
        { title: "About", icon: "mdi-account-question", to: "about" },
        { title: "Post", icon: "mdi-pen", to: "posts" }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
</style>