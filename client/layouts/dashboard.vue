<template>
  <v-app>
    <admin-bar />

    <v-content>
      <nuxt />
    </v-content>
  </v-app>
</template>

<script>
import AdminBar from "~/components/Admin/HeadBar";
export default {
  components: { AdminBar }
};
</script>
