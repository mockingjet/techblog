<template>
  <v-app>
    <app-bar />
    <v-content>
      <nuxt />
    </v-content>
    <app-foo />
  </v-app>
</template>

<script>
import AppBar from "~/components/Default/AppBar";
import AppFoo from "~/components/Default/AppFoo";
export default {
  components: { AppBar, AppFoo }
};
</script>
