from django.db import models

# Create your models here.
class Category(models.Model):
	categoryName = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.categoryName}'


class SubCategory(models.Model):
	subCategoryName=models.CharField(max_length=50)
	categoryName=models.ForeignKey(Category,on_delete=models.CASCADE)
	subCategoryDiscount=models.IntegerField()
	def __str__(self):
		return f'{self.subCategoryName}'


class Product(models.Model):
	productImage = models.ImageField(upload_to = "productImages/")
	productName = models.CharField(max_length=40)
	productDescription = models.TextField()
	productViewed = models.IntegerField()
	productBuyed = models.IntegerField()
	productCompany = models.CharField(max_length=100)
	productPrice = models.IntegerField()
	productDiscount = models.IntegerField()
	productAddedDate = models.DateTimeField(auto_now_add=True)
	productQuantity=models.IntegerField()
	productDiscountedPrice=models.IntegerField()
	productCategory = models.ForeignKey(Category,on_delete=models.CASCADE)
	productSubCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	avgReview=models.FloatField(default=50)
	noOfReviews=models.IntegerField(default=1)
	def __str__(self):
		return f'{self.productName}'

class User(models.Model):
	userName = models.CharField(max_length=40)
	userEmail = models.EmailField(max_length=60)
	userPassword = models.CharField(max_length=20)
	userContact = models.CharField(max_length=20)
	userAddedDate = models.DateTimeField(auto_now_add=True)
	userProducts = models.ManyToManyField(Product,related_name="userProducts")
	userCart = models.ManyToManyField(Product,related_name="userCart")
	userBuyedProducts=models.ManyToManyField(Product,related_name="userBuyedProducts")
	userAddress = models.CharField(max_length=200)
	def __str__(self):
		return f'{self.userName}'

class Review(models.Model):
	reviewTitle=models.CharField(max_length=40)
	reviewDesc=models.TextField()
	reviewRating=models.IntegerField()
	reviewUser=models.ForeignKey(User,on_delete=models.CASCADE)
	reviewProduct=models.ForeignKey(Product,on_delete=models.CASCADE)
	reviewAddedDate=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f'{self.reviewTitle} - {self.reviewTitle}'