import os
import shutil

## SET UP Input and Output 
indir = 'c:\\s'
outdir = 'c:\\s'

ts = '220859'
fromDirectory = indir + '\\' + ts

print(f"I set up {fromDirectory} as the source. \n")

# Create folder 
new_root = ts + '_Tests'
outroot = outdir + '\\' + new_root
os.mkdir(outroot)

print(f"I created {outroot} as the target. \n")

# Create subfolder 

tests_folder = outroot + '\\' + 'Tests'
os.mkdir(tests_folder)

print(f"I created the Tests folder. \n")

# Test 1

test1_folder = tests_folder + '\\' + 'Test1_Full_Clean'
if not os.path.isdir(test1_folder):
    os.mkdir(test1_folder)
    
src_test1 = os.path.join(fromDirectory,'Constructional')
dest_test1 = os.path.join(test1_folder,'Constructional') 

shutil.copytree(src_test1,dest_test1) 

shutil.rmtree(dest_test1 + '\\' + 'zzz_delete_before_fdm_use')

print(f"I created Test1. \n")


# Test 2

test2_folder = tests_folder + '\\' + 'Test2_NoCounterexamples'

shutil.copytree(test1_folder,test2_folder)

for root, dirs, files in os.walk(test2_folder): 
    for dir in dirs:
        if dir == 'CounterExamples' :
            shutil.rmtree(os.path.join(root,dir))
            
print(f"I created Test2. \n")


# Test 3

test3_folder = tests_folder + '\\' + 'Test3_NoExtraExamples'

shutil.copytree(test2_folder,test3_folder)

for root, dirs, files in os.walk(test3_folder): 
    for dir in dirs:
        if 'Extra_Examples' in dir :
            shutil.rmtree(os.path.join(root,dir))
            
print(f"I created Test3. \n")


# Test 4 

test4_folder = tests_folder + '\\' + 'Test4_Level2'

shutil.copytree(test3_folder,test4_folder)

throw = []
for dir in os.listdir(os.path.join(test4_folder, 'Constructional')):
    if not dir[0] in ['0','1','2']:
        throw.append(dir)

for root, dirs, files in os.walk(test4_folder): 
    for dir in dirs:
        if dir in throw :
            shutil.rmtree(os.path.join(root,dir))

print(f"I created Test4. \n")


# Test 5 

test5_folder = tests_folder + '\\' + 'Test5_Level1'

shutil.copytree(test4_folder,test5_folder)

throw = []
for dir in os.listdir(os.path.join(test5_folder, 'Constructional')):
    if not dir[0] in ['0','1']:
        throw.append(dir)

for root, dirs, files in os.walk(test5_folder): 
    for dir in dirs:
        if dir in throw :
            shutil.rmtree(os.path.join(root,dir))

print(f"I created Test5. \n")


# Test 6

test6_folder = tests_folder + '\\' + 'Test6_Level0'

shutil.copytree(test5_folder,test6_folder)

throw = []
for dir in os.listdir(os.path.join(test6_folder, 'Constructional')):
    if not dir[0] in ['0']:
        throw.append(dir)

for root, dirs, files in os.walk(test6_folder): 
    for dir in dirs:
        if dir in throw :
            shutil.rmtree(os.path.join(root,dir))

print(f"I created Test6. \n")


# Test 7 

test7_folder = tests_folder + '\\' + 'Test7_Plurals'

shutil.copytree(test6_folder,test7_folder)

for root, dirs, files in os.walk(test7_folder): 
    for dir in dirs:
        if dir == '01_Common' :
            shutil.rmtree(os.path.join(root,dir))

print(f"I created Test7. \n")


# Test 8

test8_folder = tests_folder + '\\' + 'Test8_Plurals_Core'

shutil.copytree(test7_folder,test8_folder)

for root, dirs, files in os.walk(test8_folder): 
    for dir in dirs:
        if dir == 'PartialIdentity' :
            shutil.rmtree(os.path.join(root,dir))

print(f"I created Test8. \n")

print(f"I am done. \n")