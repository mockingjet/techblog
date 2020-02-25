<template>
  <div class="pop-section">
    <v-row>
      <v-col>
        <div class="ps-title-block">
          <h3 class="ps-title">最多文章的類別</h3>
        </div>
      </v-col>
    </v-row>
    <v-row class="ps-tags">
      <v-col v-for="i in 4" :key="i">
        <v-card class="ps-tag">
          <div class="text-center">
            <v-avatar size="100" tile>
              <img src="https://vuejs.org/images/logo.png" alt />
            </v-avatar>
          </div>
          <h4 class="text-center font-weight-bold">VueJS</h4>
          <v-card-subtitle>漸進式的Javascript前端框架，擁有優雅的開發曲線和友善的社群。</v-card-subtitle>
          <v-row class="no-gutters">
            <v-col offset="2" cols="4">
              <p class="text-center caption pt-2">40篇文章</p>
            </v-col>
            <v-col cols="4">
              <p class="text-center caption pt-2">50則留言</p>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Tag from "~/services/tag.js";
export default {
  data() {
    return {
      pop_tags: []
    };
  },
  async asyncData() {
    let data = await Tag.all();
    this.pop_tags = data;
  }
};
</script>

<style lang="scss">
.pop-section {
  .ps-title-block {
    border-bottom: 1px solid lightgray;
  }
  .ps-title {
    width: 180px;
    margin-bottom: 0px;
    padding-bottom: 15px;
    border-bottom: 2px solid rgba(0, 0, 0, 0.9);
  }
  .ps-tag {
    padding: 15px 10px;
    .caption {
      color: #666;
    }
  }
}
</style>