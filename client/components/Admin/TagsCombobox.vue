<template>
  <v-combobox
    dark
    chips
    filled
    multiple
    hide-selected
    label="文章標籤"
    background-color="#444"
    :items="items"
    item-text="tag_name"
    item-value="id"
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
        <strong>{{ item.tag_name }}</strong>
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
    this.items = data.list;
  },
  methods: {
    remove(item) {
      this.tags.splice(this.tags.indexOf(item), 1);
    }
  },
  watch: {
    tags(val, prev) {
      if (val.length == prev.length) return;

      this.tags = val.map(v => {
        if (typeof v === "string") v = { tag_name: v };
        return v;
      });

      this.$emit("update:tags", this.tags);
    }
  }
};
</script>