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
import AppDrawer from "~/components/Default/AppDrawer";
import AppBar from "~/components/Default/AppBar";
import AppFoo from "~/components/Default/AppFoo";
export default {
  components: { AppDrawer, AppBar, AppFoo },
  data() {
    return {
      drawer: true
    };
  }
};
</script>