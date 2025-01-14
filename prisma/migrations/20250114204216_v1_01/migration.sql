/*
  Warnings:

  - The `image_link` column on the `Product` table would be dropped and recreated. This will lead to data loss if there is data in the column.

*/
-- AlterTable
ALTER TABLE "Product" DROP COLUMN "image_link",
ADD COLUMN     "image_link" TEXT[];
