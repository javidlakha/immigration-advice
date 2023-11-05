#!/usr/bin/env node
import "source-map-support/register"
import * as cdk from "aws-cdk-lib"
import { Construct } from "constructs"
import { aws_apigateway as apigateway, aws_lambda as lambda } from "aws-cdk-lib"

export class API extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const backend = new lambda.DockerImageFunction(this, "backend", {
      code: lambda.DockerImageCode.fromImageAsset(".", {
        cmd: ["api.main.handler"],
      }),
      environment: {
        STAGE: "prod",
      },
      memorySize: 1769,
      timeout: cdk.Duration.seconds(60),
    })

    const api = new apigateway.LambdaRestApi(this, "api", {
      handler: backend,
    })
  }
}

const app = new cdk.App()
new API(app, "API", {})
