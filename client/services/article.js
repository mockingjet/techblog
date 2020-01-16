import request from "~/plugins/axios"

const all = async () => {
  try {
    const { data = {} } = await request.get('/articles')
    return data.list
  } catch (err) {
    console.log(err)
    return {}
  }
}

const add = async (
  params = {
    title,
    tags,
    preview,
    content
  }
) => {
  const { data = {} } = await request.post('/articles', params)
  return data.id || false
}

const get = async (id) => {
  try {
    const { data = {} } = await request.get(`/articles/${id}`)
    return data
  } catch (err) {
    console.log(err)
    return {}
  }
}

const set = () => {

}

const cut = () => {

}

export default { all, add, get, set, cut }