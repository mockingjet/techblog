<template>
  <div>
    <v-row>
      <v-col cols="6">
        <v-card
          v-if="new_articles[0]"
          @click="$router.push(`/articles/${new_articles[0].article_id}`)"
        >
          <v-img
            style="width:100%; height:200px"
            class="white--text align-end"
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
          ></v-img>
          <v-card-title style="font-size:28px;">{{new_articles[0].title}}</v-card-title>
          <v-card-subtitle class="pt-1">{{dateToString(new_articles[0].created_at)}}</v-card-subtitle>
          <v-card-text class="text--primary">
            <div style="height:70px">{{truncateString(new_articles[0].preview)}}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="6">
        <v-row class="no-gutters" v-for="(post,i) in new_articles.slice(1)" :key="i">
          <v-col>
            <v-card class="mb-4" @click="$router.push(`/articles/${post.article_id}`)">
              <v-row>
                <v-col cols="3" class="py-0">
                  <v-img
                    style="width:100%; height:115px"
                    class="white--text align-end"
                    :src="`https://cdn.vuetifyjs.com/images/cards/${imgs[i]}.jpg`"
                  ></v-img>
                </v-col>
                <v-col cols="9" class="py-0">
                  <v-card-title>{{post.title}}</v-card-title>
                  <v-card-subtitle class="pb-1">{{dateToString(post.created_at)}}</v-card-subtitle>
                  <v-card-text class="text--primary">
                    <div class="ellipsis">{{post.preview}}</div>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Article from "~/services/article.js";
export default {
  data() {
    return {
      new_articles: [],
      imgs: ["docks", "house", "road", "plane"]
    };
  },
  async created() {
    let data = await Article.all();
    this.new_articles = data;
  },
  methods: {
    dateToString(date) {
      const [day, m, d, y] = new Date(date).toDateString().split(" ");
      return [m, d].join(" ");
    },
    truncateString(string) {
      let tmp = string.split("");
      tmp.length = 70;
      return tmp.join("") + "...";
    }
  }
};
</script>

<style lang="scss">
.ellipsis {
  letter-spacing: 0.5px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>