<template>
  <v-combobox
    dark
    chips
    filled
    multiple
    hide-selected
    label="文章標籤"
    persistent-hint
    background-color="#444"
    :items="items"
    v-model="tags"
  >
    <template v-slot:selection="{ attrs, item, select, selected }">
      <v-chip
        close
        label
        color="primary"
        v-bind="attrs"
        :input-value="selected"
        @click="select"
        @click:close="remove(item)"
      >
        <strong>{{ item }}</strong>
      </v-chip>
    </template>
  </v-combobox>
</template>
<script>
import Tag from "~/services/tag.js";
export default {
  data() {
    return {
      tags: [],
      items: []
    };
  },
  async created() {
    let data = await Tag.all();
    this.items = data;
  },
  methods: {
    remove(item) {
      this.tags.splice(this.tags.indexOf(item), 1);
      this.tags = [...this.tags];
    }
  },
  watch: {
    tags(value) {
      this.$emit("update:tags", value);
    }
  }
};
</script>