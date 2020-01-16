<template>
  <v-container>
    <section v-for="(article,i) in articles" :key="i">
      <v-card class="mb-8">
        <v-card-actions>
          <v-list-item class="grow">
            <v-list-item-avatar color="grey darken-3">
              <v-img
                class="elevation-6"
                src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
              ></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>Evan You</v-list-item-title>
              <v-list-item-subtitle>
                <small>{{article.date}}</small>
              </v-list-item-subtitle>
            </v-list-item-content>
            <v-row align="center" justify="end">
              <v-icon class="mr-1">mdi-comment</v-icon>
              <v-icon class="mr-1">mdi-checkbox-multiple-blank</v-icon>
              <v-icon class="mr-1">mdi-heart-outline</v-icon>
              <!-- <v-icon class="mr-1" color="red">mdi-heart</v-icon> -->
              <v-icon class="mr-1">mdi-pencil-box</v-icon>
            </v-row>
          </v-list-item>
        </v-card-actions>

        <v-card-title>
          <span class="headline font-weight-boldt">{{article.title}}</span>
        </v-card-title>

        <v-card-text class="title font-weight-medium">
          <span>{{article.preview}}</span>
        </v-card-text>

        <v-card-actions>
          <v-row align="center" justify="start" class="pl-6 pb-3">
            <v-chip small class="mr-1" v-for="(tag, i) in article.tags" :key="i">{{tag}}</v-chip>
          </v-row>
          <v-row align="center" justify="end" class="pr-6 pb-3">
            <v-btn small color="red" dark nuxt :to="`/articles/${article.id}`">more</v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </section>
  </v-container>
</template>

<script>
import Article from "~/services/article.js";
export default {
  async asyncData() {
    let data = await Article.all();
    return {
      articles: data
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