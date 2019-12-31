<template>
  <v-container>
    <v-row class="align-cneter justfiy-center">
      <v-col v-for="(item, i) in items" :key="i">
        <item-card :item="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "~/plugins/axios";
import ItemCard from "~/components/Home/ItemCard.vue";
export default {
  components: {
    ItemCard
  },
  head() {
    return {
      title: "TechBlog"
    };
  },
  data() {
    return {
      items: [
        {
          title: "Frontend",
          icon: "mdi-home",
          link: "/topic/Frontend",
          subtitle: "研究前端技術"
        },
        {
          title: "Backend",
          icon: "mdi-account-question",
          link: "/topic/Backend",
          subtitle: "研究後端技術"
        },
        {
          title: "DevOps",
          icon: "mdi-pen",
          link: "/topic/Devops",
          subtitle: "研究系統架構"
        }
      ]
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