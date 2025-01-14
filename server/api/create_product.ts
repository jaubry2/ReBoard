import { createProduct } from "../data/product";

export default defineEventHandler(async (event) => {
  const {
    url,
    title,
    price,
    image_link,
    description,
  } = await readBody(event);
  try {
    const new_product_id = await createProduct(url, title, price, image_link, description);
    return { id: new_product_id };
  } catch (error) {
    console.log(error);
    throw error;
  }
});
