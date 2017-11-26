# a='{}{}'
# b=a.format("affiliate-staging.ap-southeast-1.elasticbeanstalk.com/api/v2/","hotels/get_availability")
# print(b)

name="abin"
surname="shakya"

description="{}'s surname is {}"

description=description.format(name,surname)
print(description)