<template>
  <v-container>
    <v-row>
      <v-col offset="1" cols="8">
        <nuxt-child />
      </v-col>
      <v-col offset="1" cols="2">
        <v-list shaped class="tags-list">
          <v-card-title>技術標籤</v-card-title>
          <v-divider />
          <v-list-item-group color="primary" class="tags-group">
            <v-list-item v-for="(tag, i) in tags" :key="i">
              <v-list-item-content>
                <v-list-item-title>{{tag.tag_name}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Tag from "~/services/tag.js";
export default {
  async asyncData() {
    let data = await Tag.all();
    return {
      tags: data
    };
  }
};
</script>

<style lang="scss" scoped>
.tags-list {
  position: fixed;
  .tags-group {
    height: calc(100vh - 220px);
    overflow-y: auto;
  }
}
</style>