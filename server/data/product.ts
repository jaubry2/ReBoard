import prisma from "./prisma";

/* Requete qui créer un produits */
/* Params 
    url : String
    title : String
    price : number
    image_link : String[]
    description : String
*/
/* Return : number */
export async function createProduct(
    url: string,
    title: string,
    price: GLfloat,
    image_link: String[],
    description: string,
  ) {
    try {
      const new_product = await prisma.product.create({
        data: {
          url: url,
        title: title,
        price: price,
        image_link: image_link,
        description: description,
        },
      });
      return new_product.id;
    } catch (error) {
      console.error(error);
      throw error;
    } finally {
      // Fermer la connexion à la base de données
      await prisma.$disconnect();
    }
  }