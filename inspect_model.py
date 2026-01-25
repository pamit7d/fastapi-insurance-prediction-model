import pickle
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print(f"Model Type: {type(model)}")
    if hasattr(model, 'steps'):
        print("Pipeline Steps:")
        for step_name, step_obj in model.steps:
            print(f"  - {step_name}: {type(step_obj)}")
    else:
        print("Not a Pipeline.")
except Exception as e:
    print(f"Error loading model: {e}")
