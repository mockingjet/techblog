<template>
  <v-container fluid class="ma-0 pa-0" style="position:relative">
    <!-- Article -->
    <v-row class="no-gutters pb-12 post-form" align="center" justify="center">
      <v-container>
        <v-col cols="10" offset="1">
          <v-text-field dark filled label="文章標題" background-color="#444" v-model="post.title" />
          <tags-combobox :tags.sync="post.tags" />
          <v-textarea
            dark
            filled
            :rows="6"
            auto-grow
            label="文章預覽"
            background-color="#444"
            v-model="post.preview"
          />
          <v-row justify="center">
            <v-btn
              fab
              dark
              color="info"
              @click="$vuetify.goTo(
                '.viewer', {
                easing:'linear', 
                duration:300, 
                offset:0
              })"
            >
              <v-icon>mdi-arrow-down-bold</v-icon>
            </v-btn>
          </v-row>
        </v-col>
      </v-container>
    </v-row>

    <!-- MarkDown -->
    <v-row class="no-gutters makr">
      <v-col cols="6">
        <client-only placeholder="Loading...">
          <codemirror class="editor" v-model="post.content" :options="cmOpts" />
        </client-only>
      </v-col>
      <v-col cols="6">
        <div class="viewer">
          <div v-html="$md.render(post.content)"></div>
        </div>
      </v-col>
    </v-row>

    <!-- Submit  -->
    <v-btn absolute dark fab right color="red" style="bottom:15px" @click="addArticle">
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </v-container>
</template>

<script>
import Article from "~/services/article.js";
import TagsCombobox from "~/components/Admin/TagsCombobox";
export default {
  layout: "dashboard",
  components: { TagsCombobox },
  data() {
    return {
      cmOpts: {
        tabSize: 2,
        mode: "markdown",
        theme: "monokai",
        lineNumbers: true,
        lineWrapping: true
      },
      post: {
        title: "",
        tags: [],
        preview: "",
        content: ""
      }
    };
  },
  methods: {
    async addArticle() {
      const article_id = await Article.add(this.post);
      if (article_id) this.$router.push("/articles/1");
      else alert("error");
    }
  }
};
</script>

<style lang="scss">
$gap: calc(100vh - 64px);
.post-form {
  height: $gap;
}
.editor {
  font-size: 110%;
  width: 100%;
  .CodeMirror {
    height: $gap !important;
  }
}
.viewer {
  width: 100%;
  height: $gap !important;
  overflow-y: auto;
  padding: 0px 10px;
  code {
    overflow-x: auto !important;
    color: rgb(209, 217, 225) !important;
    padding: 0.5em !important;
    background: rgb(71, 73, 73) !important;
  }
}
</style>