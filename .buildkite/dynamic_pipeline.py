from buildkite_sdk import CommandStep, Pipeline

pipeline = Pipeline()
pipeline.add_step(
    CommandStep(
        commands=[
            "echo 'Hello, world!'",
            "false",
        ],
    )
)
# pipeline.add_step(CommandStep(commands="false"))

# JSON output
# print(pipeline.to_json())
# YAML output
print(pipeline.to_yaml())
