1. Find a way to schedule tasks in partitions 

5/30
1. BUGs happen when #partition = 1, #threads = 1
2. Trying to get a level list of circuits(mimic \_build\_prop\_cands), sort each level according to the number of successors. (Store this level list as a 2-D vector). Try to do this to btask only first
3. Finish level lists, now store it in a 1-D vector(blevel of pins in discending order), but I didn't sort each level for now
4. I am thinking: traverse this 1-D vector of pins to fill up my partitions. Then use an atomic counter to count how many tasks have left for this level, if there is no task left for this partition, then this partition will go to do the task in next level
5. As for the centralized pending task queue, I need to think about it more clearly
6. Store the number of pins per level per partition, ready to modify Timer::\_build\_partitioned\_taskflow


5/31
1. Finish each partition try to finish the task in one level instead of waiting. Performance did not improve...

