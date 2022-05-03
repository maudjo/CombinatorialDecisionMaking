import pymzn;
import pathlib;

def ConvertToDzn(instance):
    file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/"+ instance, "w+")
    #her må vi prøve å lese filene i instances og konvertere til dictionaries som vi så konverterer til dzn
    #data = {'a': [2,3], 'b': {4, 6}, 'c': {1, 2, 3}, 'd': {3: 4.5, 4: 1.3}, 'e': [[1, 2], [3, 4], [5, 6]]}
    #pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/'+instance)
    file.close()

initial_count = 0
for path in pathlib.Path("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances").iterdir():
    if path.is_file():
        initial_count += 1

print(initial_count)


#for i in range(4):
#   ConvertToDzn("ins"+str(i+1)+".dzn")
