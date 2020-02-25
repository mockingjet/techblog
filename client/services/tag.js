import request from "~/plugins/axios"

const all = async () => {
  try {
    const { data = {} } = await request.get('/tags')
    return data.list
  } catch (err) {
    console.log(err)
    return {}
  }
}

const getPop4 = async () => {
  try {
    const { data = {} } = await request.get('/tags')
    return data.list
  } catch (err) {
    console.log(err)
    return {}
  }
}

export default { all, getPop4 }