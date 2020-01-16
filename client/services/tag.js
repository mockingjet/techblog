import request from "~/plugins/axios"

const all = async () => {
  try {
    const { data = {} } = await request.get('/tags')
    return data
  } catch (err) {
    console.log(err)
    return {}
  }
}

const add = async (

) => {

}

const get = async (id) => {

}

const set = () => {

}

const cut = () => {

}

export default { all, add, get, set, cut }