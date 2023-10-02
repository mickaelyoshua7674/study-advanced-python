from rx import from_iterable
from rx import operators as op

# # Simple print
# obs = from_iterable(range(4)) # from_iterable return an Observable
# obs.subscribe(on_next=lambda x: print(f"Next item: {x}"),
#               on_completed=lambda: print("No more data"))

# # map operator
# obs = from_iterable(range(4)).pipe(op.map(lambda x: x**2))
# obs.subscribe(on_next=lambda x: print(f"Next item: {x}"),
#               on_completed=lambda: print("No more data"))



# group_by
obs = from_iterable(range(4)).pipe(op.group_by(lambda x: x%2))
obs.subscribe(on_next=lambda x: print(f"Next item: {x}"),
              on_completed=lambda: print("No more data"))
print()
# show key of groups
obs.subscribe(lambda x: print(f"group key {x.key}"))
print()
# get serult from specific group
obs.pipe(op.take(1)).subscribe(lambda x: x.subscribe(print)) # pipeline to group key 1 then get the observable and print value in 'x.subscribe(print)'