<template>
  <v-container>
    <new-section />
    <pop-section />
  </v-container>
</template>

<script>
import axios from "~/plugins/axios";
import NewSection from "~/components/Home/NewSection";
import PopSection from "~/components/Home/PopSection";
export default {
  components: {
    NewSection,
    PopSection
  },
  head() {
    return {
      title: "TechBlog"
    };
  },
  data() {
    return {};
  }
};
</script>
