"use client";

import { Editor } from "@/components/editor";
import { ImpactsInScopeManager } from "@/components/impactsInScopeManager";
import { RewardsByThreatLevelManager } from "@/components/rewardsByThreatLevelManager";
import { Separator } from "@/components/ui/separator";
import { Button } from "@/components/ui/button";
import { useState } from "react";
import { AssetsInScopeManager } from "@/components/assetsInScopeManager";
import { siteConfig } from "@/config/site";

export default function CreateBountyPage() {
	const [editor1Content, setEditor1Content] = useState("");
	const [editor2Content, setEditor2Content] = useState("");
	const [editor3Content, setEditor3Content] = useState("");
	const [editor4Content, setEditor4Content] = useState("");
	const [editor5Content, setEditor5Content] = useState("");

	const [criticalReward, setCriticalReward] = useState([]);
	const [highReward, setHighReward] = useState([]);
	const [mediumReward, setMediumReward] = useState([]);
	const [lowReward, setLowReward] = useState([]);

	const [impacts, setImpacts] = useState([]);
	const [assets, setAssets] = useState([]);

	// Submit the bounty to the server
	async function handleSubmit(e) {
		e.preventDefault();

		const res = await fetch(`${siteConfig.backendURL}/bounties`, {
			method: "POST",
			body: JSON.stringify({
				overview: editor1Content,
				rewards: {
					text: editor2Content,
					categories: {
						critical: criticalReward,
						high: highReward,
						medium: mediumReward,
						low: lowReward,
					},
				},
				assets: { text: editor3Content, assets: assets },
				impacts: { text: editor4Content, impacts: impacts },
				outOfScope: editor5Content,
			}),
		}).catch((err) => console.error(err));
	}

	return (
		<form
			onSubmit={handleSubmit}
			className="flex flex-col items-center space-y-8"
		>
			<h1>Create a Bounty</h1>
			<p className="mb-4">
				Please fill out the fields below accordingly to fit your
				requirements.
			</p>
			<Separator className="my-4 w-7/12" />
			<div className="flex flex-col items-center w-full">
				<h3>Program Overview</h3>
				<Editor setEditorContent={setEditor1Content} />
			</div>
			<Separator className="my-4 w-7/12" />
			<div className="flex flex-col items-center w-full">
				<h3>Rewards by Threat Level</h3>
				<Editor setEditorContent={setEditor2Content} />
				<RewardsByThreatLevelManager
					setCriticalReward={setCriticalReward}
					setHighReward={setHighReward}
					setMediumReward={setMediumReward}
					setLowReward={setLowReward}
				/>
			</div>
			<Separator className="my-4 w-7/12" />
			<div className="flex flex-col items-center w-full">
				<h3>Assets in Scope</h3>
				<AssetsInScopeManager assets={assets} setAssets={setAssets} />
				<Editor setEditorContent={setEditor3Content} />
			</div>
			<Separator className="my-4 w-7/12" />
			<div className="flex flex-col items-center w-full">
				<h3>Impacts in Scope</h3>
				<ImpactsInScopeManager
					impacts={impacts}
					setImpacts={setImpacts}
				/>
				<Editor setEditorContent={setEditor4Content} />
			</div>
			<Separator className="my-4 w-7/12" />
			<div className="flex flex-col items-center w-full">
				<h3>Out of Scope & Rules</h3>
				<Editor setEditorContent={setEditor5Content} />
			</div>
			<Button type="submit">Submit Bounty</Button>
		</form>
	);
}
